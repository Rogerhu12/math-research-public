#!/usr/bin/env python3
"""Bounded exact recovery from T96 NF coefficients to the original 17 equations."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

ORIGINAL_D = "23366320238786911411830138211362846399922176000"
ORIGINAL_CONTENTS = [
    "6191736422400", "12383472844800", "6191736422400", "6191736422400",
    "3095868211200", "6191736422400", "6191736422400", "6191736422400",
    "3095868211200", "30958682112000", "3095868211200", "48372940800",
    "48372940800", "6191736422400", "193491763200", "154793410560", "773967052800"
]
INPUT_SHA = "291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"
NF_SHA = "eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840"
DAG_SHA = {
    "forward.bin": "66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e",
    "backward.bin": "cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f",
    "reduction.bin": "e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b"
}

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        while block := stream.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coefficients", type=Path, required=True)
    parser.add_argument("--coefficient-receipt", type=Path, required=True)
    parser.add_argument("--nf-dir", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--seconds", type=int, default=60)
    parser.add_argument("--memory-mib", type=int, default=512)
    a = parser.parse_args()
    if a.seconds < 1 or a.memory_mib <= 0:
        raise ValueError("positive explicit time and memory limits required")
    a.work.mkdir(parents=True, exist_ok=True)
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    source = root / "2026-11-14-r150-original-seventeen-t96-lift-789f.cpp"
    header = root / "2026-11-14-r150-f31-bitplane-789f.hpp"
    def choose_original_file(names):
        for name in names:
            candidate = a.nf_dir / name
            if candidate.exists():
                return candidate
        raise FileNotFoundError("missing original NF input: " + ", ".join(names))
    nf_receipt_path = choose_original_file(("normal-form-receipt.json", "native-normal-form-receipt.json"))
    nf = json.loads(nf_receipt_path.read_text())
    lifted = json.loads(a.coefficient_receipt.read_text())
    stats = lifted.get("nativeStatistics") or {}
    if (nf.get("status") != "completed" or not nf.get("allSources")
        or nf.get("sourceCount") != 2195 or nf.get("targetCount") != 9
        or nf["options"].get("basisMode") != "rref"
        or nf.get("inputSHA256") != INPUT_SHA
        or nf["outputs"]["normal-forms.bin"]["sha256"] != NF_SHA
        or nf.get("originalCommonDenominator") != ORIGINAL_D
        or nf.get("constantRowContents") != ORIGINAL_CONTENTS
        or lifted.get("status") != "completed" or lifted.get("field") != 31
        or lifted.get("inputSHA256") != NF_SHA
        or lifted.get("sourceShiftRule") != "degree(R_j)-96"
        or lifted.get("maximumProductDegree") != 146
        or stats.get("status") != "original-nine-targets-low-degree-lift-complete"
        or stats.get("fullNormalFormSourceIdentity") is not True
        or stats.get("allDegreeBoundsVerified") is not True):
        raise ValueError("completed full original T96 NF source identity and exact original NF receipt required")
    model = choose_original_file(("normal-form-input.txt", "native-normal-form-input.txt"))
    if sha(model) != INPUT_SHA:
        raise ValueError("original seventeen-equation model hash changed")
    dag_files = {}
    for suffix, expected in DAG_SHA.items():
        path = a.nf_dir / ("nf-" + suffix)
        if sha(path) != expected or nf["outputs"][suffix]["sha256"] != expected:
            raise ValueError("original constant prebasis or normal-form provenance changed: " + suffix)
        dag_files[suffix] = path
    coefficient_record = lifted["outputs"]["original-coefficients.bin"]
    coefficient_hash = sha(a.coefficients)
    if a.coefficients.suffix == ".gz":
        if coefficient_hash != coefficient_record["gzipSHA256"]:
            raise ValueError("gzip original-source coefficient hash")
        with gzip.open(a.coefficients, "rb") as stream:
            coefficients = stream.read(5000001)
    else:
        coefficients = a.coefficients.read_bytes()
    if (len(coefficients) > 5000000 or len(coefficients) != coefficient_record["bytes"]
        or hashlib.sha256(coefficients).hexdigest() != coefficient_record["sha256"]):
        raise ValueError("complete original-source coefficient payload")
    plain_input = a.work / "normal-form-source-coefficients.bin"
    plain_input.write_bytes(coefficients)
    denominator_residue = int(ORIGINAL_D) % 31
    content_residues = [int(value) % 31 for value in ORIGINAL_CONTENTS]
    if not denominator_residue or any(not value for value in content_residues):
        raise ValueError("original row normalization has a nonunit mod 31")
    scales = a.work / "original-row-scales.txt"
    scales.write_text(" ".join(map(str, [denominator_residue] + content_residues)) + "\n")
    receipt = {
        "format": "r150-original-seventeen-t96-lift-run-v1", "field": 31, "status": "preparing",
        "sourceCoefficientSHA256": coefficient_record["sha256"],
        "sourceCoefficientReceiptSHA256": sha(a.coefficient_receipt),
        "normalFormReceiptSHA256": sha(nf_receipt_path), "modelSHA256": INPUT_SHA,
        "normalFormInputSHA256": NF_SHA, "dagSHA256": DAG_SHA,
        "originalCommonDenominator": ORIGINAL_D, "originalConstantRowContents": ORIGINAL_CONTENTS,
        "originalDenominatorResidue": denominator_residue, "originalContentResidues": content_residues,
        "coefficientDegreeBound": 136, "maximumProductDegree": 146,
        "cppSHA256": sha(source), "runnerSHA256": sha(__file__), "arithmeticHeaderSHA256": sha(header),
        "compileOptions": ["-O2", "-std=c++17"], "secondsLimit": a.seconds,
        "memoryMiBLimit": a.memory_mib, "outputs": {}
    }
    receipt_file = a.out / "original-seventeen-lift-receipt.json"
    def save():
        receipt_file.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    binary = a.work / "original-seventeen-lift"
    compiled = subprocess.run([
        "timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--",
        "g++", "-O2", "-std=c++17", str(source), "-o", str(binary)
    ], capture_output=True, text=True)
    if compiled.returncode:
        receipt.update(status="compile-failed", compileOutput=compiled.stdout + compiled.stderr)
        save()
        print(receipt["compileOutput"])
        raise SystemExit(1)
    receipt.update(status="running", binarySHA256=sha(binary))
    save()
    prefix = a.work / "original"
    command = ["timeout", "--kill-after=10s", f"{a.seconds}s", "prlimit",
               f"--as={a.memory_mib*1024*1024}", "--core=0", "--", str(binary),
               str(plain_input), str(model), str(dag_files["reduction.bin"]),
               str(dag_files["forward.bin"]), str(dag_files["backward.bin"]), str(scales), str(prefix)]
    started = time.monotonic()
    child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (a.out / "original-seventeen-lift.log").open("w") as log:
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
    complete = (code == 0 and last.get("status") == "full-original-seventeen-lift-complete"
                and last.get("field") == 31 and last.get("maximumCoefficientDegree", 137) <= 136
                and last.get("fullOriginalSeventeenEquationIdentity") is True
                and last.get("fullOriginalMacaulayIdentity") is True
                and last.get("originalRowScaleTransportVerified") is True)
    receipt.update(status="completed" if complete else "failed-or-incomplete", exitCode=code,
                   elapsedSeconds=time.monotonic()-started, nativeStatistics=last)
    if complete:
        plain = Path(str(prefix) + "-seventeen-coefficients.bin")
        zipped = a.work / "original-seventeen-coefficients.bin.gz"
        zipped.write_bytes(gzip.compress(plain.read_bytes(), mtime=0))
        record = {"bytes": plain.stat().st_size, "sha256": sha(plain),
                  "gzipBytes": zipped.stat().st_size, "gzipSHA256": sha(zipped)}
        if zipped.stat().st_size <= 5000000:
            destination = a.out / "original-seventeen-coefficients.bin.gz"
            shutil.copyfile(zipped, destination)
            record.update(gzipFile=str(destination), storage="repository-sized-gzip")
        else:
            # Preserve the complete compressed stream in ordered repository-
            # sized parts. Concatenating these bytes recovers the exact gzip.
            parts = []
            combined = hashlib.sha256()
            offset = 0
            with zipped.open("rb") as stream:
                while block := stream.read(4000000):
                    number = len(parts) + 1
                    destination = a.out / f"original-seventeen-coefficients.bin.gz.part{number:03d}"
                    destination.write_bytes(block)
                    combined.update(block)
                    parts.append({"index": number, "file": destination.name, "offset": offset,
                                  "bytes": len(block), "sha256": sha(destination)})
                    offset += len(block)
            if offset != record["gzipBytes"] or combined.hexdigest() != record["gzipSHA256"]:
                raise ValueError("complete gzip part stream failed its aggregate hash")
            manifest = {
                "format": "r150-original-seventeen-gzip-parts-v1",
                "reconstruction": "Concatenate parts in increasing index, verify full gzip SHA256, then decompress.",
                "plainBytes": record["bytes"], "plainSHA256": record["sha256"],
                "gzipBytes": record["gzipBytes"], "gzipSHA256": record["gzipSHA256"],
                "maximumPartBytes": 4000000, "parts": parts
            }
            manifest_path = a.out / "original-seventeen-coefficients.parts.json"
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
            record.update(storage="complete-repository-sized-gzip-parts", parts=parts,
                          manifestFile=str(manifest_path), manifestSHA256=sha(manifest_path))
        receipt["outputs"]["original-seventeen-coefficients.bin"] = record
        metadata = a.out / "original-seventeen-coefficients.json"
        shutil.copyfile(Path(str(prefix) + "-seventeen-coefficients.json"), metadata)
        receipt["outputs"]["metadata"] = {"file": str(metadata), "bytes": metadata.stat().st_size, "sha256": sha(metadata)}
    save()
    print(json.dumps(receipt))
    if not complete:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
