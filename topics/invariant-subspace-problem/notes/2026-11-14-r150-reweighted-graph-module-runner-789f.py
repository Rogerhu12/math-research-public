#!/usr/bin/env python3
"""One bounded, fixed T=96 reweighting of the complete original T=64 graph."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

INPUT_SHA = "eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840"
OLD_GRAPH_SHA = "70e625ca0f0a217117d588dd673f0f8aeafc407d8f33cff0ba1c6e6e9d9d9bdb"
REFERENCE_BASIS_SHA = "0b397a7fe10f27d9c8ec9453e654ce52c0d1499187e1cc6cb2228d3676159960"

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        while block := stream.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--graph", type=Path, required=True)
    p.add_argument("--graph-receipt", type=Path, required=True)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--nf-receipt", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--seconds", type=int, default=900)
    p.add_argument("--soft-seconds", type=float, default=840)
    p.add_argument("--memory-mib", type=int, default=4096)
    a = p.parse_args()
    if a.seconds < 1 or not 0 < a.soft_seconds < a.seconds or a.memory_mib < 256:
        raise ValueError("explicit positive bounded compute and adequate one-copy memory required")
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    source = root / "2026-11-14-r150-reweighted-graph-module-789f.cpp"
    header = root / "2026-11-14-r150-f31-bitplane-789f.hpp"
    reference_path = root / "2026-11-14-r150-native-graded-module-gb-full-receipt-789f.json"
    graph = json.loads(a.graph_receipt.read_text())
    nf = json.loads(a.nf_receipt.read_text())
    reference = json.loads(reference_path.read_text())
    graph_hash = sha(a.graph)
    input_hash = sha(a.input)
    stats = graph.get("nativeStatistics") or {}
    if (graph.get("status") not in ("completed", "full-graph-without-elimination")
        or graph.get("exitCode") != 0 or stats.get("processedSources") != 2195
        or stats.get("outputLeadingRows") != 1021 or stats.get("sourceLeadingRows") != 1174
        or graph.get("inputSHA256") != INPUT_SHA or input_hash != INPUT_SHA
        or graph_hash != OLD_GRAPH_SHA or graph["outputs"]["basis.bin"]["sha256"] != graph_hash
        or nf.get("status") != "completed" or not nf.get("allSources")
        or nf["outputs"]["normal-forms.bin"]["sha256"] != INPUT_SHA
        or reference.get("status") != "completed" or reference.get("inputSHA256") != INPUT_SHA
        or reference["nativeStatistics"]["basisRows"] != 1021
        or reference["outputs"]["basis.ssi"]["sha256"] != REFERENCE_BASIS_SHA):
        raise ValueError("exact complete original graph, linked NF and reference full output GB required")
    receipt = {
        "format": "r150-fixed-t96-reweighted-graph-run-v1", "field": 31, "status": "preparing",
        "inputSHA256": input_hash, "inputGraphSHA256": graph_hash,
        "inputGraphReceiptSHA256": sha(a.graph_receipt), "nfReceiptSHA256": sha(a.nf_receipt),
        "referenceCompleteGBReceiptSHA256": sha(reference_path),
        "referenceCompleteGBBasisSHA256": REFERENCE_BASIS_SHA,
        "referenceCompleteGBOutputDegreeSum": 716,
        "oldSourceShiftRule": "degree(R_j)-64", "sourceShiftRule": "degree(R_j)-96",
        "maximumWeightedRowDegree": 8, "wordsPerPlane": 4842,
        "fullSingleCopyBasisBytes": 212563800,
        "cppSHA256": sha(source), "runnerSHA256": sha(__file__), "arithmeticHeaderSHA256": sha(header),
        "secondsLimit": a.seconds, "softSeconds": a.soft_seconds, "memoryMiBLimit": a.memory_mib,
        "outputs": {}
    }
    path = a.out / "reweighted-graph-receipt.json"
    def save():
        path.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    binary = a.out / "reweighted-graph"
    compile_result = subprocess.run([
        "timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--",
        "g++", "-O3", "-std=c++17", str(source), "-o", str(binary)
    ], capture_output=True, text=True)
    if compile_result.returncode:
        receipt.update(status="compile-failed", compileOutput=compile_result.stdout + compile_result.stderr)
        save()
        print(receipt["compileOutput"])
        raise SystemExit(1)
    receipt.update(binarySHA256=sha(binary), status="running")
    save()
    prefix = a.out / "reweighted"
    started = time.monotonic()
    command = ["timeout", "--kill-after=10s", f"{a.seconds}s", "prlimit",
               f"--as={a.memory_mib*1024*1024}", "--core=0", "--",
               str(binary), str(a.graph), str(prefix), str(a.soft_seconds)]
    child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (a.out / "reweighted-graph.log").open("w") as log:
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
    last = events[-1] if events else {}
    all_rows = code == 0 and last.get("processedSources") == 2195 and last.get("status") in (
        "complete-reweighted-graph-projection-basis", "complete-reweighted-graph-projection-not-certified")
    certified = all_rows and last.get("projectionSpanCertified") is True and last.get("outputDegreeSum") == 716
    receipt.update(status="completed" if certified else (
        "full-graph-without-projection-certificate" if all_rows else "failed-or-prefix"),
        exitCode=code, elapsedSeconds=time.monotonic()-started, allOriginalGraphRowsProcessed=all_rows,
        projectionSpanCertified=certified, nativeStatistics=last)
    for suffix in ("basis.bin", "metadata.json"):
        output = Path(str(prefix) + "-" + suffix)
        if output.exists():
            receipt["outputs"][suffix] = {"file": str(output), "bytes": output.stat().st_size, "sha256": sha(output)}
    save()
    print(json.dumps(receipt))
    if not all_rows:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
