#!/usr/bin/env python3
"""Bounded original weighted-RHS normal forms, preserving the exact prebasis."""
import argparse, gzip, hashlib, json, subprocess, time
from pathlib import Path

MODEL = "291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"
DAG = {
    "forward.bin": "66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e",
    "backward.bin": "cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f",
}

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        while b := f.read(1048576):
            h.update(b)
    return h.hexdigest()

def main():
    p = argparse.ArgumentParser()
    for name in ("model", "rhs", "rhs-receipt", "out"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--binary", type=Path)
    p.add_argument("--seconds", type=int, default=60)
    p.add_argument("--memory-mib", type=int, default=512)
    a = p.parse_args()
    if a.seconds < 1 or a.memory_mib < 1:
        raise ValueError("explicit positive resource bounds required")
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    source = root / "2026-11-14-r150-original-rhs-normal-form-789f.cpp"
    r = json.loads(a.rhs_receipt.read_text())
    if r.get("status") != "completed" or r.get("nativeStatistics", {}).get("initialOriginalPrimitiveIdentityMod31") is not True:
        raise ValueError("actual completed original first residual required")
    if sha(a.model) != MODEL:
        raise ValueError("original primitive model changed")
    record = r["outputs"]["first-residual.bin"]
    payload = a.rhs.read_bytes()
    if a.rhs.suffix == ".gz":
        if hashlib.sha256(payload).hexdigest() != record["gzipSHA256"]:
            raise ValueError("compressed RHS checksum")
        payload = gzip.decompress(payload)
    if hashlib.sha256(payload).hexdigest() != record["sha256"]:
        raise ValueError("complete original residual checksum")
    rhs = a.out / "original-rhs-input.bin"
    rhs.write_bytes(payload)
    receipt = {
        "format": "r150-original-rhs-normal-form-run-v1", "status": "preparing",
        "prime": 31, "weightedOutputBudget": 85,
        "originalModelSHA256": MODEL, "rhsSHA256": record["sha256"],
        "rhsReceiptSHA256": sha(a.rhs_receipt), "cppSHA256": sha(source),
        "runnerSHA256": sha(__file__), "secondsLimit": a.seconds,
        "memoryMiBLimit": a.memory_mib, "outputs": {}, "correctionComputed": False,
    }
    rp = a.out / "original-rhs-normal-form-receipt.json"
    def save():
        rp.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    binary = a.binary or a.out / "original-rhs-normal-form"
    if not a.binary:
        result = subprocess.run(["timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--", "g++", "-O2", "-std=c++17", str(source), "-o", str(binary)], capture_output=True, text=True)
        if result.returncode:
            receipt.update(status="compile-failed", compileOutput=result.stdout + result.stderr)
            save()
            raise SystemExit(1)
    receipt.update(status="running", binarySHA256=sha(binary))
    save()
    prefix = a.out / "rhs"
    start = time.monotonic()
    child = subprocess.Popen(["timeout", "--kill-after=10s", f"{a.seconds}s", "prlimit", f"--as={a.memory_mib * 1048576}", "--core=0", "--", str(binary), str(a.model), str(rhs), str(prefix)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (a.out / "original-rhs-normal-form.log").open("w") as log:
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
    complete = code == 0 and last.get("status") == "native-original-rhs-normal-forms-complete" and last.get("sources") == 0 and last.get("targets") == 9
    receipt.update(status="completed" if complete else "failed-or-incomplete", exitCode=code, elapsedSeconds=time.monotonic()-start, nativeStatistics=last)
    if complete:
        for name in ("forward.bin", "backward.bin", "normal-forms.bin", "reduction.bin"):
            f = Path(str(prefix) + "-" + name)
            record = {"file": str(f), "bytes": f.stat().st_size, "sha256": sha(f)}
            if name in DAG:
                if record["sha256"] != DAG[name]:
                    receipt.update(status="prebasis-provenance-mismatch")
                    save()
                    raise ValueError("the original prebasis changed")
            else:
                g = a.out / (name + ".gz")
                g.write_bytes(gzip.compress(f.read_bytes(), mtime=0))
                if g.stat().st_size > 5000000:
                    raise ValueError("bounded RHS artifact exceeds file limit")
                record.update(gzipFile=str(g), gzipBytes=g.stat().st_size, gzipSHA256=sha(g))
            receipt["outputs"][name] = record
        receipt["sameOriginalConstantPrebasis"] = True
    save()
    print(json.dumps(receipt))
    if not complete:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
