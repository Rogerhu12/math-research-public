#!/usr/bin/env python3
"""One bounded exact test of the fixed original standard-source image."""
import argparse, gzip, hashlib, json, subprocess, time
from pathlib import Path

GRAPH = "bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce"
ORIGINAL_NF = "eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840"

def sha(p):
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        while b := f.read(1048576):
            h.update(b)
    return h.hexdigest()

def main():
    p = argparse.ArgumentParser()
    for name in ("graph", "original-nf", "rhs-nf", "rhs-receipt", "out"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--binary", type=Path)
    p.add_argument("--seconds", type=int, default=60)
    p.add_argument("--memory-mib", type=int, default=512)
    a = p.parse_args()
    if a.seconds < 1 or a.memory_mib < 1:
        raise ValueError("positive explicit bounds required")
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    source = root / "2026-11-14-r150-original-rhs-standard-solver-789f.cpp"
    r = json.loads(a.rhs_receipt.read_text())
    if r.get("status") != "completed" or r.get("sameOriginalConstantPrebasis") is not True:
        raise ValueError("actual complete original RHS normal form required")
    if sha(a.graph) != GRAPH or sha(a.original_nf) != ORIGINAL_NF:
        raise ValueError("complete original image/kernel source data changed")
    record = r["outputs"]["normal-forms.bin"]
    payload = a.rhs_nf.read_bytes()
    if a.rhs_nf.suffix == ".gz":
        if hashlib.sha256(payload).hexdigest() != record["gzipSHA256"]:
            raise ValueError("compressed original RHS NF checksum")
        payload = gzip.decompress(payload)
    if hashlib.sha256(payload).hexdigest() != record["sha256"]:
        raise ValueError("original RHS NF checksum")
    rhs = a.out / "rhs-normal-form-input.bin"
    rhs.write_bytes(payload)
    receipt = {
        "format": "r150-original-rhs-standard-source-run-v1", "status": "preparing",
        "prime": 31, "fixedOriginalSourceBudget": 85, "temporarySourceBudget": 181,
        "graphSHA256": GRAPH, "originalNFSHA256": ORIGINAL_NF,
        "rhsNFSHA256": record["sha256"], "rhsReceiptSHA256": sha(a.rhs_receipt),
        "cppSHA256": sha(source), "runnerSHA256": sha(__file__),
        "secondsLimit": a.seconds, "memoryMiBLimit": a.memory_mib,
        "outputs": {}, "originalCorrectionTransported": False,
    }
    rp = a.out / "original-rhs-standard-source-receipt.json"
    def save():
        rp.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    binary = a.binary or a.out / "original-rhs-standard-solver"
    if not a.binary:
        result = subprocess.run(["timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--", "g++", "-O2", "-std=c++17", str(source), "-o", str(binary)], capture_output=True, text=True)
        if result.returncode:
            receipt.update(status="compile-failed", compileOutput=result.stdout+result.stderr)
            save()
            raise SystemExit(1)
    receipt.update(status="running", binarySHA256=sha(binary))
    save()
    prefix = a.out / "solve"
    start = time.monotonic()
    child = subprocess.Popen(["timeout", "--kill-after=10s", f"{a.seconds}s", "prlimit", f"--as={a.memory_mib*1048576}", "--core=0", "--", str(binary), str(a.graph), str(rhs), str(a.original_nf), str(prefix)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (a.out / "original-rhs-standard-source.log").open("w") as log:
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
    complete = code == 0 and last.get("status") == "original-rhs-standard-source-test-complete" and last.get("fullNormalFormDecompositionIdentity") is True and last.get("standardKernelNormalForm") is True
    receipt.update(status="completed" if complete else "failed-or-incomplete", exitCode=code, elapsedSeconds=time.monotonic()-start, nativeStatistics=last)
    if complete:
        for suffix in ("standard-coefficients.bin", "image-remainders.bin"):
            f = Path(str(prefix)+"-"+suffix)
            g = a.out / (suffix+".gz")
            g.write_bytes(gzip.compress(f.read_bytes(), mtime=0))
            if g.stat().st_size > 5000000:
                raise ValueError("bounded source artifact exceeds file limit")
            receipt["outputs"][suffix] = {"file": str(f), "bytes": f.stat().st_size, "sha256": sha(f), "gzipFile": str(g), "gzipBytes": g.stat().st_size, "gzipSHA256": sha(g)}
        f = Path(str(prefix)+"-standard-source.json")
        receipt["outputs"]["metadata"] = {"file": str(f), "bytes": f.stat().st_size, "sha256": sha(f)}
        receipt["fixedSourceImageTestPassed"] = last["fixedSourceImageTestPassed"]
    save()
    print(json.dumps(receipt))
    if not complete:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
