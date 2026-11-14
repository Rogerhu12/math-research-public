#!/usr/bin/env python3
"""One bounded canonical-source computation using the complete actual T96 kernel."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import time

INPUT_SHA = "eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840"

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        while block := stream.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()

def main():
    p = argparse.ArgumentParser()
    for name in ("graph", "graph-receipt", "coefficients", "coefficient-receipt", "input", "out"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--binary", type=Path)
    p.add_argument("--seconds", type=int, default=60)
    p.add_argument("--memory-mib", type=int, default=512)
    a = p.parse_args()
    if a.seconds < 1 or a.memory_mib <= 0:
        raise ValueError("positive explicit limits required")
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    source = root / "2026-11-14-r150-kernel-standard-source-789f.cpp"
    graph = json.loads(a.graph_receipt.read_text())
    old = json.loads(a.coefficient_receipt.read_text())
    gs = graph.get("nativeStatistics") or {}
    os = old.get("nativeStatistics") or {}
    graph_hash = sha(a.graph)
    if (graph.get("status") != "completed" or not graph.get("projectionSpanCertified")
        or gs.get("processedSources") != 2195 or gs.get("outputDegreeSum") != 716
        or gs.get("sourceLeadingRows") != 1174 or gs.get("sourceLeadingRowsWithNonzeroOutput") != 0
        or graph["outputs"]["basis.bin"]["sha256"] != graph_hash
        or graph.get("inputSHA256") != INPUT_SHA or sha(a.input) != INPUT_SHA
        or old.get("status") != "completed" or old.get("inputSHA256") != INPUT_SHA
        or old.get("graphSHA256") != graph_hash
        or os.get("fullNormalFormSourceIdentity") is not True
        or os.get("allDegreeBoundsVerified") is not True):
        raise ValueError("complete linked original T96 graph, actual zero-output kernel and nine-target identity required")
    record = old["outputs"]["original-coefficients.bin"]
    payload = a.coefficients.read_bytes()
    if a.coefficients.suffix == ".gz":
        if hashlib.sha256(payload).hexdigest() != record["gzipSHA256"]:
            raise ValueError("compressed coefficient hash")
        payload = gzip.decompress(payload)
    if len(payload) != record["bytes"] or hashlib.sha256(payload).hexdigest() != record["sha256"]:
        raise ValueError("complete original coefficient payload")
    plain = a.out / "input-original-coefficients.bin"
    plain.write_bytes(payload)
    receipt = {
        "format": "r150-kernel-standard-source-run-v1", "field": 31, "status": "preparing",
        "graphSHA256": graph_hash, "graphReceiptSHA256": sha(a.graph_receipt),
        "inputSHA256": INPUT_SHA, "sourceCoefficientSHA256": record["sha256"],
        "sourceCoefficientReceiptSHA256": sha(a.coefficient_receipt),
        "cppSHA256": sha(source), "runnerSHA256": sha(__file__),
        "arithmeticHeaderSHA256": sha(root / "2026-11-14-r150-f31-bitplane-789f.hpp"),
        "weightedSourceBudget": 146, "secondsLimit": a.seconds, "memoryMiBLimit": a.memory_mib,
        "outputs": {}
    }
    path = a.out / "kernel-standard-source-receipt.json"
    def save():
        path.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    binary = a.binary or a.out / "kernel-standard-source"
    if a.binary is None:
        result = subprocess.run(["timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912",
            "--core=0", "--", "g++", "-O3", "-std=c++17", str(source), "-o", str(binary)],
            capture_output=True, text=True)
        if result.returncode:
            receipt.update(status="compile-failed", compileOutput=result.stdout + result.stderr)
            save()
            print(receipt["compileOutput"])
            raise SystemExit(1)
    receipt.update(status="running", binarySHA256=sha(binary),
                   compileMode="provided-binary" if a.binary else "bounded-O3-compile")
    save()
    started = time.monotonic()
    prefix = a.out / "kernel"
    child = subprocess.Popen(["timeout", "--kill-after=10s", f"{a.seconds}s", "prlimit",
        f"--as={a.memory_mib*1024*1024}", "--core=0", "--", str(binary), str(a.graph), str(plain),
        str(a.input), str(prefix)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (a.out / "kernel-standard-source.log").open("w") as log:
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
    complete = (code == 0 and last.get("status") == "canonical-original-source-complete"
        and last.get("fullNormalFormSourceIdentity") is True
        and last.get("standardKernelNormalForm") is True
        and last.get("minimalWeightedSourceCost") is True)
    receipt.update(status="completed" if complete else "failed-or-incomplete", exitCode=code,
                   elapsedSeconds=time.monotonic()-started, nativeStatistics=last)
    if complete:
        original = Path(str(prefix) + "-canonical-coefficients.bin")
        compressed = a.out / "canonical-original-coefficients.bin.gz"
        compressed.write_bytes(gzip.compress(original.read_bytes(), mtime=0))
        if compressed.stat().st_size > 5000000:
            raise ValueError("canonical coefficient artifact exceeded repository limit")
        receipt["outputs"]["canonical-coefficients.bin"] = {
            "bytes": original.stat().st_size, "sha256": sha(original), "gzipFile": str(compressed),
            "gzipBytes": compressed.stat().st_size, "gzipSHA256": sha(compressed)}
        metadata = Path(str(prefix) + "-canonical-coefficients.json")
        receipt["outputs"]["metadata"] = {"file": str(metadata), "bytes": metadata.stat().st_size, "sha256": sha(metadata)}
    save()
    print(json.dumps(receipt))
    if not complete:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
